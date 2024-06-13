import { inject } from 'vue';

export function useErrorHandler() {
    const triggerError = inject('triggerError');
    if (!triggerError) {
        throw new Error('triggerError n\'est pas fourni');
    }

    return {
        triggerError
    };
}
