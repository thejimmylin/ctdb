<template>
  <h1>{{ meta.verboseName }}</h1>
  <section>
    <ModelTable v-bind:model="model" />
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
      meta: {
        model:{
          name: "news",
        },
        fields: [
         {name: "title"},
         {name: "content"},
        ]
      }
    }
  },
  computed: {
    model() {
      return {name: this.meta.model.name}
    }
  }
};
</script>
