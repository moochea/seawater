<template>
  <v-app>
      <AppBar
              :get-last-operation-message=getLastOperationMessage
              :get-server-busy=getServerBusy
              :get-last-operation-status="getLastOperationStatus"/>
    <v-main>
      <Home></Home>
    </v-main>
  </v-app>
</template>

<script>
  import Home from './components/Home';
  import {mapGetters, mapMutations} from "vuex";
  import AppBar from "@/components/AppBar";

  export default {
    name: 'App',

    components: {
      AppBar,
      Home
    },

    data: () => ({
    }),
    computed: {
      ...mapGetters('commandStore', ['getServerBusy', 'getLastOperationMessage', 'getLastOperationStatus'])
    },
    methods: {
      ...mapMutations('commandStore', ['setViewPortSize']),
      saveViewPortDimensions () {
        this.setViewPortSize({width: window.innerWidth, height: window.innerHeight})
      }
    },
    created() {
      window.addEventListener('resize', this.saveViewPortDimensions, {passive: true})
    },
    mounted() {
      this.saveViewPortDimensions()
    }
  };

</script>

<style>
  html {
    overflow-y: auto;
  }
</style>
