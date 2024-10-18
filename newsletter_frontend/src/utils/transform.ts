import { ApiUser } from '../types/api';
import { User } from '../types/auth';

export function transformUser(apiUser: ApiUser): User {
    return {
        id: apiUser.id,
        email: apiUser.email,
        firstName: apiUser.first_name,
        lastName: apiUser.last_lame,
    };
}
