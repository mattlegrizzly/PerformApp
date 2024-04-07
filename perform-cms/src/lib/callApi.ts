import type IERequestOptions from "@/types/request"
import type {IEUser, IEUserData} from '@/types/types'

const baseUrl = 'http://127.0.0.1:8000/'

const handleParams = (url : URL, options : IERequestOptions) => {
    if (typeof options.search !== "undefined") {
        Object.keys(options.search).map((searchProperty : any) => {
            const searchValues = options.search[searchProperty]

            if (Array.isArray(searchValues)) {
                searchValues.map((searchValue) => url.searchParams.append(searchProperty, searchValue))
            } 
        })
    }

    if (typeof options.itemsPerPage !== "undefined") {
        url.searchParams.set("itemsPerPage", options.itemsPerPage)
    }

    if (typeof options.page !== "undefined") {
        url.searchParams.set("page", options.page)
    }
}

const handleResponse = (response : Response, tryRefresh : boolean) => {
    if(tryRefresh === false) {
        response.json().then((data) => {
            console.log(' la res ',  data)
            if (data['code'] === "token_not_valid" ) {
                refresh().then((data) => {
                    console.log('data ' , data)
                })
            } else if(!response.ok){
                console.log('error')
                throw 'Error'
            } else {
                console.log('data')
                return data
            }
        })
    } else {
        throw Error('error credentials')
    }
}

const refresh = async () : Promise<any> => {
    const relativeUrlString = "/api/refresh_tokens/"
    const url = new URL(relativeUrlString, baseUrl);
    const user = JSON.parse(localStorage.getItem('user') as string) as IEUser;
    const body = {
        refresh : user.refresh
    };

    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const request = new Request(url, {
        method: "POST",
        headers,
        body: JSON.stringify(body),
    })

    const response = await fetch(request);
    handleResponse(response, true);
}

/**
 * This function permits to do some get request with React Query
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const get = async (urlChunk : string , options = {} as IERequestOptions, authorization = true) : Promise<any> => {
    const relativeUrlString = "/api" + urlChunk
    const url = new URL(relativeUrlString, baseUrl)

    handleParams(url, options)

    const headers = new Headers()

    if (authorization) {
        let token = sessionStorage.getItem("user") || localStorage.getItem("user") || ""
        token = JSON.parse(token)["access"]
        headers.append("Authorization", `Bearer ${token}`)
    }

    const request = new Request(url, {
        method: "GET",
        headers: headers,
    })

    fetch(request).then((response) => {
        console.log('response ' , response)
        handleResponse(response, false)
    })

}

const post = async (urlChunk : String, options = {} as IERequestOptions, authorization = false) => {
    const relativeUrlString = "/api" + urlChunk
    const url = new URL(relativeUrlString, baseUrl)

    handleParams(url, options)

    const headers = new Headers()

    if (urlChunk.includes("recipes")) {
        // For FormData, we don't set Content-Type header,
        // it will be set automatically along with boundary
    } else {
        headers.append("Content-Type", "application/json")
    }

    if (authorization) {
        let token = ""
        if (localStorage.getItem("user")) {
            token = localStorage.getItem("user") as string
        }
        if (sessionStorage.getItem("user")) {
            token = sessionStorage.getItem("user") as string
        }
        token = JSON.parse(token)["access"]
        headers.append("Authorization", `Bearer ${token}`)
    }

    let body
    if (urlChunk.includes("recipes")) {
        const formData = new FormData()

        Object.entries(options.body).forEach((field) => {
            formData.append(field[0], field[1])
        })

        body = formData
    } else {
        body = JSON.stringify(options.body)
    }

    const request = new Request(url, {
        method: "POST",
        headers: headers,
        body: body,
    })

    const response = await fetch(request)

    return handleResponse(response, false)
}

/**
 * This function permits to do some put request to the API
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const put = async (urlChunk : string, options = {} as IERequestOptions, authorization = true) => {
    const relativeUrlString = "/api" + urlChunk
    const url = new URL(relativeUrlString, baseUrl)

    handleParams(url, options)

    const headers = new Headers()
    let token = sessionStorage.getItem("user") || localStorage.getItem("user") || ""
    token = JSON.parse(token)["access"]

    headers.append("Content-Type", "application/json")
    if (authorization) {
        headers.append("Authorization", `Bearer ${token}`)
    }

    const request = new Request(url, {
        method: "PUT",
        headers: headers,
        body: JSON.stringify(options.body),
    })

    const response = await fetch(request)
    return handleResponse(response, false)
}

/**
 * This function permits to do some patch request to the API
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const patch = async (urlChunk : string, options = {} as IERequestOptions, authorization = true) => {
    const relativeUrlString = "/api" + urlChunk
    const url = new URL(relativeUrlString, baseUrl)

    handleParams(url, options)

    const headers = new Headers()

    if (urlChunk.includes("recipes")) {
        // For FormData, we don't set Content-Type header,
        // it will be set automatically along with boundary
    } else {
        headers.append("Content-Type", "application/json")
    }

    if (authorization) {
        let token = ""
        if (localStorage.getItem("user")) {
            token = localStorage.getItem("user") as string
        }
        if (sessionStorage.getItem("user")) {
            token = sessionStorage.getItem("user") as string
        }
        token = JSON.parse(token)["access"]
        headers.append("Authorization", `Bearer ${token}`)
    }

    let body
    if (urlChunk.includes("recipes")) {
        const formData = new FormData()

        Object.entries(options.body).forEach((field) => {
            formData.append(field[0], field[1])
        })

        body = formData
    } else {
        body = JSON.stringify(options.body)
    }

    const request = new Request(url, {
        method: "PATCH",
        headers: headers,
        body: body,
    })

    const response = await fetch(request)

    return handleResponse(response, false)
}

/**
 * This function permits to do delete request to the API
 * @param {*} urlChunk
 * @param {*} authorization
 */
const del = async (urlChunk : any, authorization = true) => {
    const url = new URL(urlChunk, baseUrl)

    const headers = new Headers()

    let token : string = sessionStorage.getItem("user") || localStorage.getItem("user") || ""
    token = JSON.parse(token)["access"]

    headers.append("Content-Type", "application/json")
    if (authorization) {
        headers.append("Authorization", `Bearer ${token}`)
    }

    // headers.append('Access-Control-Allow-Origin', '*')

    const request = new Request(url, {
        method: "DELETE",
        headers: headers,
    })

    await fetch(request)
}

export { get, post, put, del, patch, refresh }