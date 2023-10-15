<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<ConversationDetailsList />
		<Conversation />
	</div>
</template>

<script>
	import ConversationDetailsList from '../../components/conversation/ConversationsDetailsList.vue';
	import Conversation from '../../components/conversation/Conversation.vue';
	export default {
		name: 'ConversationView',
		components: {
			ConversationDetailsList,
			Conversation,
		},
		setup() {
			return {};
		},
	};
</script>

<style lang="postcss" scoped></style>
