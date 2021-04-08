<template>
  <section class="container max-w-full justify-center">
    <h1 class="text-green-900">{{ tableTitle }}</h1>
    <ModelTable :fields="fields" />
  </section>
</template>

<script>
import ModelTable from "@/components/ModelTable.vue";

export default {
  name: "News",
  components: {
    ModelTable,
  },
  data() {
    return {
      tableTitle: "News",
      fields: [
        {name: "id", verboseName: "ID"},
        {name: "title", verboseName: "Title"},
        {name: "content", verboseName: "Content"},
        {name: "at", verboseName: "At"},
        {name: "created_by", verboseName: "Created by"},
      ]
    }
  },
};
</script>
