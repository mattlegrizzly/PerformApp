import type IERequestOptions from '@/types/request'
import type { IEUser, IEUserData } from '@/types/types'
import { useUserStore } from '@/stores/store'
import { useCookies } from '@vueuse/integrations/useCookies'

const cookies = useCookies(['locale'])

const baseUrl = 'http://127.0.0.1:8000/'

const verifyToken = async () => {
  const access = cookies.get('access')
  const relativeUrlString = '/api/token/verify/'
  const url = new URL(relativeUrlString, baseUrl)

  const body = JSON.stringify({
    token: access
  })

  const headers = new Headers()
  headers.append('Content-Type', 'application/json')
  const request = new Request(url, {
    method: 'POST',
    headers,
    body: body
  })

  const response = await fetch(request)
  if (response.status == 401) {
    const resRefresh = await response.json()
    if (response.status > 300) {
      return {
        status: response.status,
        data: resRefresh
      }
    } else {
      return resRefresh // Retourne les données normalement si le token est valide
    }
  } else {
    return response
  }
}

const handleParams = (url: URL, options: IERequestOptions) => {
  if (typeof options.search !== 'undefined' && options && options.search) {
    Object.keys(options.search).map((searchProperty: any) => {
      //@ts-expect-error
      const searchValues = options.search[searchProperty]

      if (Array.isArray(searchValues)) {
        searchValues.map((searchValue) => url.searchParams.append(searchProperty, searchValue))
      }
    })
  }

  if (typeof options.itemsPerPage !== 'undefined') {
    url.searchParams.set('itemsPerPage', options.itemsPerPage)
  }

  if (typeof options.page !== 'undefined') {
    url.searchParams.set('page', options.page)
  }
}

const handleResponse = async (response: Response): Promise<any> => {
  const data = await response.json()
  if (response.status > 300) {
    return {
      status: response.status,
      data: data
    }
  } else {
    return data // Retourne les données normalement si le token est valide
  }
}

const refresh = async () => {
  const userStore = useUserStore()
  const relativeUrlString = '/api/refresh_tokens/'
  const url = new URL(relativeUrlString, baseUrl)
  const refresh = userStore.refresh
  const body = {
    refresh: refresh
  }

  const headers = new Headers()
  headers.append('Content-Type', 'application/json')
  const request = new Request(url, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })

  try {
    const response = await fetch(request)
    if (!response.ok) {
      throw new Error('La requête a échoué')
    }
    const data = await response.json()
    return data
  } catch (error) {
    throw new Error('Impossible de rafraîchir le token')
  }
}

/**
 * This function permits to do some get request with React Query
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const get = async (
  urlChunk: string,
  options = {} as IERequestOptions,
  authorization = true
): Promise<any> => {
  const relativeUrlString = '/api' + urlChunk
  const url = new URL(relativeUrlString, baseUrl)

  handleParams(url, options)

  const headers = new Headers()

  if (authorization) {
    const token = cookies.get('access')
    headers.append('Authorization', `Bearer ${token}`)
  }

  const request = new Request(url, {
    method: 'GET',
    headers: headers
  })

  const response = await fetch(request)
  return handleResponse(response)
}

const post = async (
  urlChunk: String,
  options = {} as IERequestOptions,
  authorization = false,
  image: boolean
) => {
  const relativeUrlString = '/api' + urlChunk
  const url = new URL(relativeUrlString, baseUrl)

  const headers = new Headers()
  if (!image) {
    headers.append('Content-Type', 'application/json')
  } else {
    headers.append('Accept', 'application/json')
  }
  handleParams(url, options)

  if (authorization) {
    const token = cookies.get('access')
    headers.append('Authorization', `Bearer ${token}`)
  }

  let body
  if (image) {
    const formData = new FormData()

    for (const key in options.body) {
      formData.append(key as string, options.body[key] as string)
    }
    body = formData
  } else {
    body = JSON.stringify(options.body)
  }

  const request = new Request(url, {
    method: 'POST',
    headers: headers,
    body: body
  })

  const response = await fetch(request)

  return handleResponse(response)
}

/**
 * This function permits to do some put request to the API
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const put = async (urlChunk: string, options = {} as IERequestOptions, authorization = true) => {
  const relativeUrlString = '/api' + urlChunk
  const url = new URL(relativeUrlString, baseUrl)

  handleParams(url, options)

  const headers = new Headers()
  const token = cookies.get('access')

  headers.append('Content-Type', 'application/json')
  if (authorization) {
    headers.append('Authorization', `Bearer ${token}`)
  }

  const request = new Request(url, {
    method: 'PUT',
    headers: headers,
    body: JSON.stringify(options.body)
  })

  const response = await fetch(request)
  return handleResponse(response)
}

/**
 * This function permits to do some patch request to the API
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const patch = async (urlChunk: string, options = {} as IERequestOptions, authorization = true) => {
  const relativeUrlString = '/api' + urlChunk
  const url = new URL(relativeUrlString, baseUrl)

  handleParams(url, options)

  const headers = new Headers()

  if (urlChunk.includes('recipes')) {
    // For FormData, we don't set Content-Type header,
    // it will be set automatically along with boundary
  } else {
    headers.append('Content-Type', 'application/json')
  }

  if (authorization) {
    const token = cookies.get('access')
    headers.append('Authorization', `Bearer ${token}`)
  }

  let body
  if (urlChunk.includes('recipes')) {
    const formData = new FormData()

    Object.entries(options.body).forEach((field) => {
      formData.append(field[0], field[1])
    })

    body = formData
  } else {
    body = JSON.stringify(options.body)
  }

  const request = new Request(url, {
    method: 'PATCH',
    headers: headers,
    body: body
  })

  const response = await fetch(request)

  return handleResponse(response)
}

/**
 * This function permits to do delete request to the API
 * @param {*} urlChunk
 * @param {*} authorization
 */
const del = async (urlChunk: any, authorization = true) => {
  const url = new URL(urlChunk, baseUrl)

  const headers = new Headers()

  const token = cookies.get('access')

  headers.append('Content-Type', 'application/json')
  if (authorization) {
    headers.append('Authorization', `Bearer ${token}`)
  }

  // headers.append('Access-Control-Allow-Origin', '*')

  const request = new Request(url, {
    method: 'DELETE',
    headers: headers
  })

  await fetch(request)
}

export { get, post, put, del, patch, refresh, verifyToken }
