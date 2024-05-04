interface IERequestOptions {
    search? : Array<string>,
    page? : string,
    itemsPerPage? : string,
    orderBy? : string,
    body : Array<string|blob> | {},
}

export default IERequestOptions