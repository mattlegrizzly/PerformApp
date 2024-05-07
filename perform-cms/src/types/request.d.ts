interface IERequestOptions {
    search? : Array<string>,
    page? : string,
    itemsPerPage? : string,
    orderBy? : string,
    material_id? : string,
    sport_id? : string,
    workzone_code? : string,
    body : Array<string|blob|number> | {} | [],
}


export default IERequestOptions;