<template>
  <section>
    <h1>Diaries</h1>
    <Table v-bind:model="{name: 'diary'}"/>
  </section>
</template>

<script>
import Table from "@/components/Table.vue";

export default {
  name: "Diary",
  components: {
    Table,
  },
};
</script>
