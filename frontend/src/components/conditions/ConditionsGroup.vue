<doc>
  A component to create parsing conditions that could then
  be used in the backend to intelligently parse and html page
</doc>

<template>
  <div class="p-3 bg-special rounded">
    <single-condition v-for="(condition, i) in conditions" :key="i" :index="i" :condition="condition" :class="{ 'mt-3': i > 0 }" @update:condition="handeUpdateCondition" @delete:condition="handleDeleteCondition" />

    <hr>
  
    <div class="d-flex mt-3">
      <button type="button" class="btn btn-light shadow-none" @click="addCondition">
        <font-awesome-icon icon="fa-solid fa-plus" class="me-2" />
        Add condition
      </button>
    </div>
  </div>
</template>

<script>
import { ref, provide } from 'vue'
import SingleCondition from './SingleCondition.vue'

export default {
  name: 'ConditionsGroup',
  components: {
    SingleCondition
  },
  setup () {
    const conditions = ref([{ tag: null, attrs: [] }])
    provide('conditions', conditions)
    return {
      conditions
    }
  },
  methods: {
    addCondition () {
      this.conditions.push({ tag: 'body' })
    },
    handeUpdateCondition (condition) {
      this.conditions[condition[0]] = condition[1]
    },
    handleDeleteCondition (index) {
      this.conditions.splice(index, 1)
    }
  }
}
</script>

<style scoped>
.bg-special {
  background-color: rgba(108, 117, 125, .1);
}
</style>
