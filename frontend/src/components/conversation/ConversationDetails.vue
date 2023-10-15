<template>
	<div
		:class="[
			'flex',
			'items-center',
			'justify-between',
			'mt-2',
			'p-2',
			'rounded-xl',
			'cursor-pointer',
			isSelected
				? 'border-b-4 border-purple-500'
				: 'border-b-4 border-gray-300',
			isSelected ? 'shadow-purple' : 'shadow-gray',
		]"
		style="box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1)">
		<div class="flex items-center space-x-2">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-[40px] rounded-full" />
			<p class="text-xs">
				<strong>{{ otherUser.user.name }}</strong>
			</p>
		</div>
		<span class="text-xs text-gray-500">
			{{ conversation.modified_at_formatted }}
		</span>
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
			isSelected: {
				type: Boolean,
				default: false,
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

<style scoped>
	.shadow-purple {
		box-shadow: 0px 4px 4px rgba(128, 0, 128, 0.1);
	}
	.shadow-gray {
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
	}
</style>
