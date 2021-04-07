<template>
  <div class="home">
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
