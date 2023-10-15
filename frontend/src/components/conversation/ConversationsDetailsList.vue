<template>
	<div class="main-left col-span-1">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<div class="space-y-4">
                <ConversationDetails />
                <ConversationDetails />
                <ConversationDetails />
                <ConversationDetails />
			</div>
		</div>
	</div>
</template>

<script>
import ConversationDetails from './ConversationDetails.vue';
	export default {
    name: 'ConversationDetailsList',
        components: {
            ConversationDetails,
        },
		setup() {
			return {};
		},
	};
</script>

<style scoped></style>
