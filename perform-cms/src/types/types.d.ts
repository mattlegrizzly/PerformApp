interface IEUser {
  refresh : string,
  access : string, 
  user : IEUserData,
}

interface IEUserData {
    email: string
  last_name: string, 
  first_name : string,
  size: number
  age: number
  gender: string
  profile_picture: string
  sports_user: Array<String>
  user_injuries: Array<String>
  users_wellness: Array<String>
}

export default IEUser