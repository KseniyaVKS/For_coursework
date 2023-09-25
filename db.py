def change_seen(self, u_vk_id: int, p_vk_id: int):
    for u in self.session.query(User).filter(User.vk_id == u_vk_id).all():
        user_id = u.id

    for p in self.session.query(Partner).filter(Partner.vk_id == p_vk_id).all():
        partner_id = p.id

    for u_p_seen in self.session.query(User_partner.seen).filter(User_partner.user_id == user_id,
                                                                 User_partner.partner_id == partner_id).all():
        if u_p_seen[0] == 0:
            self.session.query(User_partner).filter(User_partner.user_id == user_id,
                                                    User_partner.partner_id == partner_id).update({'seen': 1})
        else:
            self.session.query(User_partner).filter(User_partner.user_id == user_id,
                                                    User_partner.partner_id == partner_id).update({'seen': 0})
        self.session.commit()