import Vue from 'vue'
import Vuex from 'vuex'
import commandStore from "@/stores/commandStore";

Vue.use(Vuex)
export default new Vuex.Store({
    modules: {commandStore}
})
