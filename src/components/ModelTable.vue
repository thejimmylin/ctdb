<template>
<table class="border-collapse">
  <thead>
    <tr>
      <th class="font-normal border border-green-600 text-green-900 p-1" v-for="(field, index) in fields" :key="index">
      {{ field.verboseName }}
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="font-normal border border-green-600 text-green-900 p-1" v-for="(field, index) in fields" :key="index">
      </td>
    </tr>
  </tbody>
</table>
</template>

<script>
export default {
  name: 'ModelTable',
  props: {
    fields: Array,
  },
}
</script>
