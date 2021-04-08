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
    <tr v-for="(result, index) in results" :key="index">
      <td class="font-normal border border-green-600 text-green-900 p-1">
        {{ result['id'] }}
      </td>
      <td class="font-normal border border-green-600 text-green-900 p-1">
        {{ result['title'] }}
      </td>
      <td class="font-normal border border-green-600 text-green-900 p-1">
        {{ result['content'] }}
      </td>
      <td class="font-normal border border-green-600 text-green-900 p-1">
        {{ result['at'] }}
      </td>
      <td class="font-normal border border-green-600 text-green-900 p-1">
        {{ result['created_by'] }}
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
    results: Array,
  },
}
</script>
