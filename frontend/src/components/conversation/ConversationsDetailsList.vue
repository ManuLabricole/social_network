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
	import { useConversationStore } from '@/stores/conversationStore';

	export default {
		name: 'ConversationDetailsList',
		components: {
			ConversationDetails,
		},
		setup() {
			const conversationStore = useConversationStore();
			return {
				conversationStore,
			};
		},
		mounted() {
			this.conversationStore.fetchConversations();
		},
	};
</script>

<style scoped></style>
