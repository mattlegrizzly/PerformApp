interface IERequestOptions {
    search? : Array<string>,
    page? : number,
    itemsPerPage? : number,
    body : Array<string|blob> | {},
}

export default IERequestOptions