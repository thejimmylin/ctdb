<template>
  <h1>{{ model.name }}</h1>
  <table>
    <thead>
      <th class="text-green-500">
      </th>
    </thead>
  </table>
</template>

<script>
export default {
  name: 'Table',
  props: {
    model: Object,
  },
}
</script>
