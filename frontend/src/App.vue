<template>
  <div id="app">
    <ul>
      <router-link tag="li" :to="{ path: '/' }" exact>
        <a>Home</a>
      </router-link>
      <router-link tag="li" :to="{ path: 'faq' }">
        <a>FAQ</a>
      </router-link>
    </ul>
    <transition name="transform" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
.router-link-active {
  border-bottom: 1px solid #2c3e50;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px auto 0;
  max-width: 100%;
  width: 800px;
}

a {
  color: #2c3e50;
  text-decoration: none;
}

a:hover {
  color: #2c3e50;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.page {
  position: fixed;
  width: inherit;
}

.transform-enter-active {
  animation: in 1s;
  animation-delay: .1s;
  opacity: 0;
}

.transform-leave-active {
  animation: out 1s;
}

@keyframes in {
  from {
    transform: translateX(-50px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes out {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(50px);
    opacity: 0;
  }
}
</style>
