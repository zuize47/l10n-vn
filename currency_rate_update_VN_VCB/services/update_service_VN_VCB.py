# © 2018 Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
import logging
from lxml import etree
from odoo.addons.currency_rate_update.services.currency_getter_interface \
    import CurrencyGetterInterface

_logger = logging.getLogger(__name__)


class VCBGetter(CurrencyGetterInterface):
    """Implementation of Currency_getter_factory interface for VCB service"""

    code = 'VN_VCB'
    name = 'Joint Stock Commercial Bank for Foreign ' \
           'Trade of Vietnam - Vietcombank'
    supported_currency_array = [
        "AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "HKD", "INR", "JPY", "KRW",
        "KWD", "MYR", "NOK", "RUB", "SAR", "SEK", "SGD", "THB", "USD", "VND"]

    def rate_retrieve(self, dom, ns, curr):
        """Parse a dom node to retrieve-currencies data"""
        xpath_rate_currency = (
            "/ExrateList/Exrate[@CurrencyCode='%s']/@Transfer"
            % curr.upper()
        )
        return {'rate_currency': float(
            dom.xpath(xpath_rate_currency, namespaces=ns)[0])}

    def get_updated_currency(self, currency_array, main_currency,
                             max_delta_days):
        """Implementation of abstract method of Curreny_getter_interface"""
        url = 'http://www.vietcombank.com.vn/ExchangeRates/ExrateXML.aspx'
        # We do not want to update the main currency
        if main_currency in currency_array:
            currency_array.remove(main_currency)
        _logger.debug("VCB currency rate service : connecting...")
        raw_file = self.get_url(url)
        dom = etree.fromstring(raw_file)
        vcb_ns = {}
        _logger.debug("VCB sent a valid XML file")
        rate_date = dom.xpath('/ExrateList/DateTime/text()',
                              namespaces=vcb_ns)[0]
        # Don't use DEFAULT_SERVER_DATE_FORMAT here, because it's
        # the format of the XML of VCB, not the format of Odoo server !
        rate_date_datetime = datetime.strptime(
            str(rate_date), '%m/%d/%Y %I:%M:%S %p')
        self.check_rate_date(rate_date_datetime, max_delta_days)
        # we dynamically update supported currencies
        self.supported_currency_array = dom.xpath(
            "/ExrateList/Exrate/@CurrencyCode", namespaces=vcb_ns)
        self.supported_currency_array.append('VND')
        _logger.debug(
            "Supported Currencies = %s " % self.supported_currency_array)
        self.validate_cur(main_currency)
        if main_currency != 'VND':
            main_curr_data = self.rate_retrieve(dom, vcb_ns, main_currency)
        for curr in currency_array:
            self.validate_cur(curr)
            if curr == 'VND':
                rate = main_curr_data['rate_currency']
            else:
                curr_data = self.rate_retrieve(dom, vcb_ns, curr)
                if main_currency == 'VND':
                    rate = curr_data['rate_currency']
                else:
                    rate = (curr_data['rate_currency'] /
                            main_curr_data['rate_currency'])
            self.updated_currency[curr] = rate
            _logger.debug(
                "Rate retrieved : 1 %s = %s %s" % (main_currency, rate, curr))
        return self.updated_currency, self.log_info
