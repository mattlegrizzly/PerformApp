import type { Order } from "./types";

interface IERequestOptions {
    search?: {
        name: string
    },
    page?: string,
    itemsPerPage?: string,
    orderBy?: Order,
    material_id?: string,
    sport_id?: string,
    workzone_code?: string,
    body: Array<string | blob | number> | {} | [] | any,
}


export default IERequestOptions;