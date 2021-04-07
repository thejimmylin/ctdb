<template>
  <p class="text-3xl text-blue-500">{{ msg }}</p>
</template>

<script>
export default {
  name: 'Message',
  props: {
    msg: String
  }
}
</script>

<style scoped>
</style>
