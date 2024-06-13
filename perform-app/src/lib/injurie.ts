/**
 * Retourne la classe CSS associée à un état.
 * @param {string} state - Le code d'état (par exemple "NT", "IP", "TR").
 * @returns {string} - La classe CSS correspondante.
 */
const stateSetClass = (state: string): string => {
    switch (state) {
        case "NT":
            return "nt_class";
        case "IP":
            return "ip_class";
        case "TR":
            return "tr_class";
        default:
            return "";
    }
};

/**
 * Retourne l'état en français en fonction du code d'état.
 * @param {string} state - Le code d'état (par exemple "NT", "IP", "TR").
 * @returns {string} - La traduction française de l'état.
 */
const stateSet = (state: string): string => {
    switch (state) {
        case "NT":
            return "Non traité";
        case "IP":
            return "En cours";
        case "TR":
            return "Traité";
        default:
            return "Non traité";
    }
};


export { stateSet, stateSetClass }