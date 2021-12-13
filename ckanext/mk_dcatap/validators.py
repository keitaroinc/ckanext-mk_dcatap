"""
Copyright (c) 2018 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from ckan.plugins.toolkit import _, get_action, request, get_validator
from ckan.logic import NotFound


not_empty = get_validator('not_empty')

def request_data_only_members_in_org_validator(key, data, errors, context):
    if not _get_request_param("metadata"):
        return
    return members_in_org_validator(key, data, errors, context)


def request_data_only_required(key, data, errors, context):
    if not _get_request_param("metadata"):
        return
    if not data.get(key):
        errors[key].append(_('Required field'))


def members_in_org_validator(key, data, errors, context):
    maintainers = data[key].split(',')
    model = context['model']
    owner_org = data.get(('owner_org',))
    if owner_org is None:
        owner_org = data.get('owner_org')
    data_dict = {
        'id': owner_org
    }
    user_ids = []
    try:
        members_in_org = get_action('member_list')(context, data_dict)
    except NotFound:
        members_in_org = []

    # member_list returns more than just users, so we need to extract only
    # users
    
    members_in_org = [member for member in members_in_org
                      if member[1] == 'user']

    for email in maintainers:
        user = model.User.by_email(email)

        if not user:
            user = model.User.get(email)

        user_found = False

        if user:
            if type(user) == list:
                user = user[0]

            for member in members_in_org:
                if member[0] == user.id:
                    user_found = True

            if user_found:
                user_ids.append(user.id)
            else:
                message = _('The user with email "{0}" is not part of this '
                            'organization.').format(email)
                errors[key].append(message)

        else:
            message = _('The user with email "{0}" does not exist.'
                        ).format(email)
            errors[key].append(message)

    data[key] = ','.join(user_ids)


def _get_request_param(param):
    try:
        return request.params.get(param)
    except (TypeError, RuntimeError):
        # In case CLI call handle RuntimeError
        return None