<template>
<div class="table">
  <table class="border-collapse">
    <thead>
      <th class="font-normal border border-green-600 text-green-900 p-1" v-for="(field, index) in fields" :key="index">
        {{ field.verboseName }}
      </th>
    </thead>
  </table>
</div>
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
