export function cleanPayload(payload: Object): Object {
    return Object.fromEntries(
        Object.entries(payload).filter(([_, value]) => value !== null && value !== undefined && value !== '')
    );
}
