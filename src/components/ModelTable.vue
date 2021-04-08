<template>
  <table>
    <thead>
      <th class="justify-self-center text-green-500 font-normal border border-gray-500" v-for="(field, index) in fields" :key="index">
        {{ field.verboseName }}
      </th>
    </thead>
  </table>
</template>

<script>
export default {
  name: 'ModelTable',
  props: {
    model: Object,
    fields: Array,
  },
}
</script>
