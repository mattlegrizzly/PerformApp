interface IEUser {
  refresh: string,
  access: string,
  user: IEUserData,
}

interface IEUserData {
  email: string
  last_name: string,
  first_name: string,
  size: number
  age: number
  gender: string
  profile_picture: string
  sports_user: Array<String>
  user_injuries: Array<String>
  users_wellness: Array<String>
}

interface Step {
  id: number,
  text: string
}

interface Muscle {
  zone: {
    code: string,
    name: string
  }
}

interface Order {
  id: string,
  value: string
}

interface QueryParams {
  query_key: string,
  array_name: any
}
export { IEUser, IEUserData, Step, Muscle, Order, QueryParams }