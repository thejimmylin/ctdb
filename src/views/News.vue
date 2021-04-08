<template>
  <h1 class="text-green-500">{{ model.verboseNamePlural }}</h1>
  <section>
    <ModelTable :model="model" :fields="fields" />
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
      model: {
        name: "news",
        verboseName: "News",
        verboseNamePlural: "News",
      },
      fields: [
        {name: "id"},
        {name: "title"},
        {name: "content"},
        {name: "at"},
        {name: "created_by"},
      ]
    }
  },
};
</script>
