<template>
	<div
		v-if="otherUser"
		class="flex items-center justify-between mt-2">
		<div class="flex items-center space-x-2">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-[40px] rounded-full" />

			<p class="text-xs">
				<strong>{{ otherUser.user.name }}</strong>
			</p>
		</div>
		<span class="text-xs text-gray-500">{{
			conversation.modified_at_formatted
		}}</span>
	</div>
</template>

<script>
	export default {
		name: 'ConversationDetails',
		props: {
			conversation: {
				type: Object,
				required: true,
			},
			currentUserId: {
				type: String,
				required: true,
			},
		},

		computed: {
			otherUser() {
				const users = this.conversation.user;
				for (let i = 0; i < users.length; i++) {
					if (users[i].user.id !== this.currentUserId) {
						console.log('otheruser', users[i]);
						return users[i];
					}
				}
				return null;
			},
		},
	};
</script>

<style scoped></style>
