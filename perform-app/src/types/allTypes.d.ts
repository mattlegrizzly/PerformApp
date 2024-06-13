interface IEUser {
  refresh: string;
  access: string;
  user: IEUserData;
}

interface IEUserData {
  email: string;
  last_name: string;
  first_name: string;
  weight: string,
  size: number;
  age: number;
  gender: string;
  profile_picture: string;
  sports_user: Array<String>;
}

interface Step {
  id: number;
  text: string;
}

interface Sport {
  id: number;
  name: string;
}

interface SportArray {
  sport: Sport
}

interface Material {
  pictures: string,
  id: string;
  name: string;
}

interface MaterialArray {
  material: Material
}


interface Muscle {
  zone: {
    code: string;
    name: string;
  };
}
interface Muscles {
  code: string;
  name: string;
}

interface Order {
  id: string;
  value: string;
}

interface QueryParams {
  query_key: string;
  array_name: any;
}

interface Injurie {
  id: string;
  name: string;
  description: string;
  zone: Muscle.zone;
  state: string;
  date: string;
}

export {
  IEUser,
  IEUserData,
  Step,
  Muscle,
  Order,
  QueryParams,
  Sport,
  Material,
  Injurie,
  Muscles,
  MaterialArray,
  SportArray
};
