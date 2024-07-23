import { defineStore } from 'pinia'
import type { IEUser, IEUserData } from '@/types/types'


export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    userData: {},
    access: '',
    refresh: ''
  }),
  getters: {
    getUser(state): IEUser {
      return {
        user: state.userData as IEUserData,
        access: state.access,
        refresh: state.refresh
      }
    },
    getAccess(state) {
      return state.access
    },
    getRefresh(state) {
      return state.refresh
    }
  },
  actions: {
    setUser(payload : any) {
      if(payload.access) {
        console.log('payload set access ', payload)
        this.userData = payload.user
        this.access = payload.access
        this.refresh = payload.refresh
      } else {
        console.log('set data')
        this.userData = payload
      }
    },
    removeUser() {
      this.userData = {} as IEUserData,
      this.access = ''
      this.refresh = ''
    },
    setTokens(payload : any) {
      this.access = payload.access
      this.refresh = payload.refresh
    }
  }
})

