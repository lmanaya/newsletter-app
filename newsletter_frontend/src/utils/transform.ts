import { ApiUser, User } from '../types';

export function transformUser(apiUser: ApiUser): User {
    return {
        id: apiUser.id,
        email: apiUser.email,
        firstName: apiUser.first_name,
        lastName: apiUser.last_lame,
    };
}
