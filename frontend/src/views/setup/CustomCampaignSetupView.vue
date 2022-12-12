<doc>
  This is a special component used to show custom settings
  related to a preset campaign that the user would have chosen.

  Depending on the campaign, the parameters change hence the
  per component view
</doc>

<template>
  <section>
    <div class="row">
      <div class="col-sm-12 col-md-12">
        <component :is="availableComponents" />
      </div>
    </div>
  </section>
</template>

<script>
import CustomCampaign from '@/components/setup/CustomCampaign.vue'

export default {
  name: 'CustomSettings',
  components: {
    CustomCampaign
  },
  computed: {
    availableComponents () {
      const routeId = this.$route.params.id
      let componentToShow
      switch (routeId) {
        case 1:
          componentToShow = 'custom-campaign'
          break
      
        default:
          componentToShow = 'custom-campaign'
          break
      }
      return componentToShow
    }
  }
}
</script>
