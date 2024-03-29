import { ref } from 'vue';

const testCount = (value : number) => {
    value = value + 1
    return value;
}

export default testCount;