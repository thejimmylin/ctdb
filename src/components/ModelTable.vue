<template>
<table class="border-collapse">
  <thead>
    <tr>
      <template v-for="(field, index) in fields" :key="index">
      <th v-if="field.isDisplayed" class="font-normal border border-green-600 text-green-900 p-1">
        {{ field.verboseName }}    
      </th>
      </template>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(result, index) in results" :key="index">
      <template v-for="(field, index) in fields" :key="index">
      <td v-if="field.isDisplayed" class="font-normal border border-green-600 text-green-900 p-1">
        {{ result[field.name] }}
      </td>
      </template>
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
