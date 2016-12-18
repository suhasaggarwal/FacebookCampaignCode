from facebookads.adobjects.customaudience import CustomAudience

lookalike = CustomAudience(parent_id='act_310419005')
lookalike.update({
    CustomAudience.Field.name: 'My lookalike audience',
    CustomAudience.Field.subtype: CustomAudience.Subtype.lookalike,
    CustomAudience.Field.lookalike_spec: {
        'ratio': 0.01,
        'country': 'IN',
        'page_id': '349224428539835',
        'conversion_type': 'page_like',
    },
})

lookalike.remote_create()
print(lookalike)