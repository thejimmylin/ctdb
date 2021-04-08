<template>
  <section class="text-center container mx-auto p-5">
    <h1 class="text-green-500">{{ model.verboseNamePlural }}</h1>
    <ModelTable :model="model" :fields="fields" />
  </section>
</template>

<script>
import ModelTable from "@/components/ModelTable.vue";

export default {
  name: "Diary",
  components: {
    ModelTable,
  },
  data() {
    return {
      model: {
        name: "diary",
        verboseName: "Diary",
        verboseNamePlural: "Diaries",
      },
      fields: [
        {name: "id", verboseName: "ID"},
        {name: "date", verboseName: "Date"},
        {name: "daily_check", verboseName: "Daily check"},
        {name: "daily_record", verboseName: "Daily record"},
        {name: "todo", verboseName: "TODO"},
        {name: "remark", verboseName: "Remark"},
        {name: "created_by", verboseName: "Created by"},
      ]
    }
  },
};
</script>
