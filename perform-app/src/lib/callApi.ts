//@ts-expect-error
import type IERequestOptions from "../types/requet";

const sendRequest = async (originalRequest: Request, originalBody: any = null, retry: boolean = true): Promise<any> => {
  try {
    const response = await fetch(originalRequest);
    if (response.status === 401 && retry && !response.url.includes('login')) {
      const refreshResponse = await refresh();
  
      if (refreshResponse && refreshResponse.access) {
        const user = await store.get("user");
        const updatedUser = {
          ...JSON.parse(user),
          access: refreshResponse.access,
        };
        await store.set("user", JSON.stringify(updatedUser));
  
        // Clone headers
        const newHeaders = new Headers(originalRequest.headers);
        newHeaders.set("Authorization", `Bearer ${refreshResponse.access}`);
  
        // Recreate the request with the new headers and the same body
        const newRequest = new Request(originalRequest.url, {
          method: originalRequest.method,
          headers: newHeaders,
          body: originalBody,
          mode: originalRequest.mode,
          credentials: originalRequest.credentials,
          cache: originalRequest.cache,
          redirect: originalRequest.redirect,
          referrer: originalRequest.referrer,
          referrerPolicy: originalRequest.referrerPolicy,
          integrity: originalRequest.integrity,
        });
        return sendRequest(newRequest, originalBody, false); // Disable retry to prevent infinite loop
      } else {
        throw new Error("Unable to refresh token");
      }
    }
    return handleResponse(response);
  } catch (error : Error | any) {
    return({
      status : 503,
      data: error.message
    })
  }
};

import { store } from "../store/store";

const baseUrl = import.meta.env.VITE_API_URL + "";

const verifyToken = async () => {
  const relativeUrlString = "/api/token/verify/";
  const url = new URL(relativeUrlString, baseUrl);
  const user = await store.get("user");
  const access = await JSON.parse(user).access;
  const body = JSON.stringify({
    token: await access,
  });

  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  const request = new Request(url, {
    method: "POST",
    headers,
    body: body,
  });

  const response = await fetch(request);
  if ((await response.status) == 401) {
    const resRefresh = await response.json();
    if ((await response.status) > 300) {
      return {
        status: response.status,
        data: resRefresh,
      };
    } else {
      return {
        status: response.status,
        data: resRefresh,
      };
    }
  } else {
    return {
      status: response.status,
      data: {},
    };
  }
};

const handleParams = (url: URL, options: IERequestOptions) => {
  if (typeof options.search !== "undefined" && options && options.search) {
    Object.keys(options.search).map(() => {
      if (options.search) {
        url.searchParams.set("search", options.search);
      }
    });
  }

  if (typeof options.itemsPerPage !== "undefined") {
    url.searchParams.set("itemsPerPage", options.itemsPerPage);
  }

  if (typeof options.page !== "undefined") {
    url.searchParams.set("page", options.page);
  }

  if (typeof options.orderBy !== "undefined") {
    url.searchParams.set("orderBy", options.orderBy.id);
  }
  if (typeof options.material_id !== "undefined") {
    url.searchParams.set("material_id", options.material_id);
  }
  if (typeof options.sport_id !== "undefined") {
    url.searchParams.set("sport_id", options.sport_id);
  }
  if (typeof options.workzone_code !== "undefined") {
    url.searchParams.set("workzone_code", options.workzone_code);
  }
};

const handleResponse = async (response: Response): Promise<any> => {
  let data;
  if(response.statusText != "No Content"){
     data = await response.json();
  }
  if (response.status > 300) {
    return {
      status: response.status,
      data: data,
    };
  } else {
    if(response.statusText != "No Content"){
      return data // Retourne les données normalement si le token est valide
   } else {
    return []
   }
  }
};

/**
 * This function permits to refresh token and User in the store
 * @returns
 */
const refresh = async (): Promise<any> => {
  const res = await store.get("user");
    const refreshToken = JSON.parse(res).refresh;
    const relativeUrlString = "/api/refresh_tokens/";
    const url = new URL(relativeUrlString, baseUrl);
    const body = { refresh: refreshToken };

    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    const request = new Request(url, {
      method: "POST",
      headers,
      body: JSON.stringify(body),
    });

    const response = await fetch(request);
    if ((await response.status) == 401) {
      const resRefresh = await response.json();
      if ((await response.status) > 300) {
        return {
          status: response.status,
          data: resRefresh,
        };
      } else {
        return {
          status: response.status,
          data: resRefresh,
        };
      }
    } else {
      return {
        status: response.status,
        data: {},
      };
    }
};

/**
 * This function permits to do some get request with Fetch
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
  const relativeUrlString = "/api" + urlChunk;
  const url = new URL(relativeUrlString, baseUrl);
  handleParams(url, options);

  const headers = new Headers();
  if (authorization) {
    const user = await store.get("user");
    const access = await JSON.parse(user).access;
    headers.append("Authorization", `Bearer ${access}`);
  }

  const request = new Request(url, {
    method: "GET",
    headers: headers,
    mode: "cors",
  });

  return sendRequest(request);
};

/**
 * This function permits to do some post request with Fetch
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @param {*} image
 * @returns
 */
const post = async (
  urlChunk: String,
  options = {} as IERequestOptions,
  authorization = false,
  image: boolean = false
) => {
  const relativeUrlString = "/api" + urlChunk;
  const url = new URL(relativeUrlString, baseUrl);

  const headers = new Headers();
  if (!image) {
    headers.append("Content-Type", "application/json");
  } else {
    headers.append("Accept", "application/json");
  }
  handleParams(url, options);

  if (authorization) {
    const user = await store.get("user");
    const access = await JSON.parse(user).access;
    headers.append("Authorization", `Bearer ${access}`);
  }

  let body;
  if (image) {
    const formData = new FormData();

    Object.entries(options.body).forEach(([key, value]) => {
      formData.append(key as string, value as string);
    });

    body = formData;
  } else {
    body = JSON.stringify(options.body);
  }

  const request = new Request(url, {
    method: "POST",
    headers: headers,
    body: body,
  });

  return sendRequest(request, body);
};

/**
 * This function permits to do some put request to the API
 * @param {*} urlChunk
 * @param {*} options
 * @param {*} authorization
 * @returns
 */
const put = async (
  urlChunk: string,
  options = {} as IERequestOptions,
  authorization = true,
  image: Boolean
) => {  
  const relativeUrlString = "/api" + urlChunk;
  const url = new URL(relativeUrlString, baseUrl);
  const headers = new Headers();
  if (!image) {
    headers.append("Content-Type", "application/json");
  } else {
    headers.append("Accept", "application/json");
  }
  handleParams(url, options);

  if (authorization) {
    const user = await store.get("user");
    const access = await JSON.parse(user).access;
    headers.append("Authorization", `Bearer ${access}`);
  }

  let body;
  if (image) {
    const formData = new FormData();

    Object.entries(options.body).forEach(([key, value]) => {
      formData.append(key as string, value as string);
    });
    body = formData;
  } else {
    body = JSON.stringify(options.body);
  }

  const request = new Request(url, {
    method: "PUT",
    headers: headers,
    body: body,
  });

  return sendRequest(request, body);
};

/**
 * This function permits to do some patch request to the API
 * @param {*} urlChunk
 * @param {Array<string>} options
 * @param {*} authorization
 * @returns
 */
const patch = async (
  urlChunk: String,
  options = {} as IERequestOptions,
  authorization = false,
  image: boolean = false
) => {
  const relativeUrlString = "/api" + urlChunk;
  const url = new URL(relativeUrlString, baseUrl);

  const headers = new Headers();
  if (!image) {
    headers.append("Content-Type", "application/json");
  } else {
    headers.append("Accept", "application/json");
  }
  handleParams(url, options);

  if (authorization) {
    const user = await store.get("user");
    const access = await JSON.parse(user).access;
    headers.append("Authorization", `Bearer ${access}`);
  }

  let body;
  if (image) {
    const formData = new FormData();

    Object.entries(options.body).forEach(([key, value]) => {
      formData.append(key as string, value as string);
    });
    body = formData;
  } else {
    body = JSON.stringify(options.body);
  }

  const request = new Request(url, {
    method: "PATCH",
    headers: headers,
    body: body,
  });
  return sendRequest(request, body);
};

/**
 * This function permits to do delete request to the API
 * @param {*} urlChunk
 * @param {*} authorization
 */
const del = async (urlChunk: any, authorization = true) => {
  verifyToken();
  const relativeUrlString = "/api" + urlChunk;
  const url = new URL(relativeUrlString, baseUrl);

  const headers = new Headers();

  headers.append("Content-Type", "application/json");
  if (authorization) {
    const user = await store.get("user");
    const access = await JSON.parse(user).access;
    headers.append("Authorization", `Bearer ${access}`);
  }

  const request = new Request(url, {
    method: "DELETE",
    headers: headers,
  });

  return sendRequest(request);
};

export { get, post, put, del, patch, refresh, verifyToken };
