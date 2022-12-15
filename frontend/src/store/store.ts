import { ref, type InjectionKey, type Ref } from 'vue'
import { createStore, Store, useStore as baseUseStore } from 'vuex'

// define your typings for the store state
export interface State {
  is_authenticated: boolean,
  stripeLoaded: Ref<boolean>
}

// define injection key
export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
  state: {
    is_authenticated: false,
    stripeLoaded: ref(false)
  },
  getters: {
    getIsAuthenticated(state) {
      return state.is_authenticated
    }
  },
  mutations: {
    setIsAuthenticated(state, value) {
      state.is_authenticated = value
    }
  },
  actions: {},
  modules: {}
})

export function useStore () {
  return baseUseStore(key)
}