<template>
  <section>
    <h1>News</h1>
    <Table v-bind:model="{name: 'news'}"/>
  </section>
</template>

<script>
import Table from "@/components/Table.vue";

export default {
  name: "News",
  components: {
    Table,
  },
};
</script>
