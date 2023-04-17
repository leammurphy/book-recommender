<template>
  <img alt="Vue logo" src="./assets/book_logo-removebg.png" class="logo">
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <BookRecommendations />
</template>

<script>
import BookRecommendations from './components/BookRecommendations.vue';


export default {
  name: 'App',
  components: {
    BookRecommendations
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #212526;
  margin-top: 15px;
}
html {
  background: #ebe8de;
  font-family: Nunito, serif;
}
.logo {
  width: 300px;
  height: 300px;
}
</style>
