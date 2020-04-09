<template>
  <div id="app">
    <Header class='header' />
    <Main class='main' />
    <Navbar class='navbar' />
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import Header from '@/components/Header.vue'
  import Main from '@/components/Main.vue'

  export default {
    name: 'turtlecreeklane',
    components: {
      Navbar, Header, Main
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
  display: grid;
  grid-template-columns: 20% 80%;
  grid-template-rows: 20% 80%;
  height: 800px;
  min-width: 770px;
  border-bottom: .5px solid gray;
}

.main {
  display: grid;
  grid-column: 2 / 3;
  grid-row: 2;
}

.header {
  display: grid;
  grid-column: 1 / 3;
  grid-row: 1 / 1;
  border-bottom: .5px solid gray;
  padding-top: 25px;
}

.navbar {
  display: grid;
  grid-column: 1 / 1;
  grid-row: 2 / 4;
  border-right: .5px solid gray;
  margin-right: -50px;
  margin-left: -50px;
}
</style>
