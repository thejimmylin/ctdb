<template>
  <div class="diary">
    <h1>This is an diary page</h1>
    <Message msg="Welcome to diary"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Message from '@/components/Message.vue'

export default {
  name: 'Diary',
  components: {
    Message
  }
}
</script>
