<template>
  <router-view :key="$route.name"></router-view>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  mounted () {
    const body = document.body
    body.classList.add('g-sidenav-show', 'bg-gray-100')
  }
}
</script>

<style>
</style>
