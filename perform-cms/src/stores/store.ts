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
    }
  },
  actions: {
    setUser(payload : any) {
      this.userData = payload.user
      this.access = payload.access
      this.refresh = payload.refresh
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

export const usePaginationStore = defineStore({
  id: 'pagination',
  state: () => ({
    materials: 1,
    sports: 1,
    users: 1,
    exercises: 1
  }),
  getters: {
    getPaginationMaterials(): number {
      return this.materials
    },
    getPaginationSports(): number {
      return this.sports
    },
    getPaginationUsers(): number {
      return this.users
    },
    getPaginationExercices(): number {
      return this.exercises
    }
  },
  actions: {
    setPaginationMaterials(payload: number) {
      this.materials += payload
    },
    setPaginationExercises(payload: number) {
      this.exercises += payload
    },
    setPaginationSports(payload: number) {
      this.sports += payload
    },
    setPaginationUsers(payload: number) {
      this.users += payload
    }
  }
})
