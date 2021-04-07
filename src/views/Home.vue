<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Message msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Message from '@/components/Message.vue'

export default {
  name: 'Home',
  components: {
    Message
  }
}
</script>
