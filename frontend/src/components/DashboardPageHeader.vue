<template>
  <div class="col-12 position-relative z-index-2">
    <base-card>
      <template #body>
        <div class="row">
          <div class="col-sm-12 col-md-12">
            <div class="d-flex justify-content-between align-items-center">
              <h2 class="fw-bolder mb-0">
                {{ title }}
              </h2>
              <slot></slot>
            </div>
          </div>
        </div>
      </template>
    </base-card>
  </div>
</template>

<script>
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'

export default {
  name: 'DashboardPageHeader',
  components: {
    BaseCard
  },
  props: {
    title: {
      type: String,
      required: true
    }
  }
}
</script>
